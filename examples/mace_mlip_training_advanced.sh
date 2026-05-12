#!/usr/bin/env bash
set -euo pipefail

# Advanced MACE MLIP fine-tuning workflow.
#
# Run from the project root, after activating an environment with mace-torch.
# Override any variable at runtime, for example:
#
#   TRAIN_FILE=data/train.xyz TEST_FILE=data/test.xyz ./examples/mace_mlip_training_advanced.sh
#
# For a multi-GPU single-node run:
#
#   NPROC_PER_NODE=4 ./examples/mace_mlip_training_advanced.sh

RUN_NAME="${RUN_NAME:-mace_omat_finetuning}"

# Input data. These are placeholders; point them at your prepared extended XYZ files.
TRAIN_FILE="${TRAIN_FILE:-data/train.xyz}"
TEST_FILE="${TEST_FILE:-data/test.xyz}"
VALID_FILE="${VALID_FILE:-}"
VALID_FRACTION="${VALID_FRACTION:-0.2}"

# Foundation model and replay data for multihead fine-tuning.
# Use a MACE model shortcut if supported by your installed version, or a path/URL to a .model file.
FOUNDATION_MODEL="${FOUNDATION_MODEL:-medium_omat}"
REPLAY_TRAIN_FILE="${REPLAY_TRAIN_FILE:-omat}"
NUM_SAMPLES_PT="${NUM_SAMPLES_PT:-30000}"
FILTER_TYPE_PT="${FILTER_TYPE_PT:-combinations}"
SUBSELECT_PT="${SUBSELECT_PT:-fps}"
WEIGHT_PT="${WEIGHT_PT:-1.0}"
ATOMIC_NUMBERS="${ATOMIC_NUMBERS:-[8, 22, 78]}"

# Dataset labels and isolated-atom reference energies.
ENERGY_KEY="${ENERGY_KEY:-ref_energy}"
FORCES_KEY="${FORCES_KEY:-ref_forces}"
E0S="${E0S:-{8:-2049.91807262, 22:-23328.13360429, 78:-518568.86288573}}"

# Optimisation and model settings.
NUM_CHANNELS="${NUM_CHANNELS:-128}"
ENERGY_WEIGHT="${ENERGY_WEIGHT:-1}"
FORCES_WEIGHT="${FORCES_WEIGHT:-100}"
LR="${LR:-0.01}"
SCALING="${SCALING:-rms_forces_scaling}"
BATCH_SIZE="${BATCH_SIZE:-4}"
VALID_BATCH_SIZE="${VALID_BATCH_SIZE:-4}"
MAX_NUM_EPOCHS="${MAX_NUM_EPOCHS:-200}"
START_SWA="${START_SWA:-150}"
EMA_DECAY="${EMA_DECAY:-0.99}"
ERROR_TABLE="${ERROR_TABLE:-PerAtomMAE}"
DEFAULT_DTYPE="${DEFAULT_DTYPE:-float64}"
DEVICE="${DEVICE:-cuda}"
SEED="${SEED:-123}"

# Set NPROC_PER_NODE > 1 to launch single-node distributed training with torchrun.
PYTHON="${PYTHON:-python}"
NPROC_PER_NODE="${NPROC_PER_NODE:-1}"
LOG_FILE="${LOG_FILE:-${RUN_NAME}.output.log}"

require_file() {
    local path="$1"
    local label="$2"
    if [[ ! -f "$path" ]]; then
        echo "Missing ${label}: ${path}" >&2
        echo "Set ${label^^} to the correct file path before running." >&2
        exit 1
    fi
}

require_file "$TRAIN_FILE" "train_file"
require_file "$TEST_FILE" "test_file"

validation_args=(--valid_fraction="$VALID_FRACTION")
if [[ -n "$VALID_FILE" ]]; then
    require_file "$VALID_FILE" "valid_file"
    validation_args=(--valid_file="$VALID_FILE")
fi

distributed_args=()
if [[ "$NPROC_PER_NODE" -gt 1 ]]; then
    train_cmd=(torchrun --standalone --nnodes=1 --nproc_per_node="$NPROC_PER_NODE" -m mace.cli.run_train)
    distributed_args=(--distributed)
else
    train_cmd=("$PYTHON" -m mace.cli.run_train)
fi

echo "Starting MACE training workflow: ${RUN_NAME}"
echo "Training data: ${TRAIN_FILE}"
echo "Test data: ${TEST_FILE}"
echo "Foundation model: ${FOUNDATION_MODEL}"
echo "Replay data: ${REPLAY_TRAIN_FILE}"
echo "Device: ${DEVICE}"
echo "Log file: ${LOG_FILE}"

time "${train_cmd[@]}" \
    --name="$RUN_NAME" \
    --num_channels="$NUM_CHANNELS" \
    --foundation_model="$FOUNDATION_MODEL" \
    --multiheads_finetuning=True \
    --train_file="$TRAIN_FILE" \
    "${validation_args[@]}" \
    --test_file="$TEST_FILE" \
    --E0s="$E0S" \
    --energy_key="$ENERGY_KEY" \
    --forces_key="$FORCES_KEY" \
    --energy_weight="$ENERGY_WEIGHT" \
    --forces_weight="$FORCES_WEIGHT" \
    --lr="$LR" \
    --scaling="$SCALING" \
    --batch_size="$BATCH_SIZE" \
    --valid_batch_size="$VALID_BATCH_SIZE" \
    --max_num_epochs="$MAX_NUM_EPOCHS" \
    --start_swa="$START_SWA" \
    --ema \
    --ema_decay="$EMA_DECAY" \
    --pt_train_file="$REPLAY_TRAIN_FILE" \
    --num_samples_pt="$NUM_SAMPLES_PT" \
    --filter_type_pt="$FILTER_TYPE_PT" \
    --subselect_pt="$SUBSELECT_PT" \
    --weight_pt="$WEIGHT_PT" \
    --atomic_numbers="$ATOMIC_NUMBERS" \
    --amsgrad \
    --swa \
    --swa_forces_weight="$FORCES_WEIGHT" \
    --error_table="$ERROR_TABLE" \
    --device="$DEVICE" \
    --default_dtype="$DEFAULT_DTYPE" \
    --seed="$SEED" \
    --restart_latest \
    "${distributed_args[@]}" \
    2>&1 | tee "$LOG_FILE"
