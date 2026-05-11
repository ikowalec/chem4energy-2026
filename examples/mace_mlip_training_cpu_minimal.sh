#!/usr/bin/env bash
set -euo pipefail

# Minimal local CPU training example for a VS Code terminal.
#
# Run from the repository root after activating your Python environment.
# The input files should be extended XYZ files with ref_energy/ref_forces labels.
#
#   TRAIN_FILE=data/train.extxyz TEST_FILE=data/test.extxyz ./examples/mace_mlip_training_cpu_minimal.sh

RUN_NAME="${RUN_NAME:-mace_cpu_minimal}"
TRAIN_FILE="${TRAIN_FILE:-data/train.extxyz}"
TEST_FILE="${TEST_FILE:-data/test.extxyz}"
PYTHON_BIN="${PYTHON:-}"

if [[ -z "$PYTHON_BIN" ]]; then
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_BIN="python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_BIN="python"
    else
        echo "Could not find python3 or python. Activate your environment first." >&2
        exit 1
    fi
fi

"$PYTHON_BIN" -m mace.cli.run_train \
    --name="$RUN_NAME" \
    --train_file="$TRAIN_FILE" \
    --valid_fraction=0.05 \
    --test_file="$TEST_FILE" \
    --E0s="average" \
    --model="MACE" \
    --num_interactions=2 \
    --num_channels=32 \
    --max_L=1 \
    --correlation=2 \
    --r_max=5.0 \
    --energy_key="ref_energy" \
    --forces_key="ref_forces" \
    --energy_weight=10 \
    --forces_weight=100 \
    --batch_size=1 \
    --valid_batch_size=1 \
    --max_num_epochs=5 \
    --eval_interval=1 \
    --ema \
    --error_table="PerAtomMAE" \
    --amsgrad \
    --default_dtype="float32" \
    --device=cpu \
    --seed=123 \
    --restart_latest \
    --save_cpu
