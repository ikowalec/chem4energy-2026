
# Minimal example of training a MACE MLIP
# Required inputs for mace fine tuning:

python mace.cli.run_train.py \
--name="fine_tuning" \
--num_channels=128 \
--foundation_model="/shared/home/mace-omat-0-medium.model" \
--multiheads_finetuning=True \
--train_file="/shared/home/training_omat/stratified_sample.xyz" \
--valid_fraction=0.2 \
--test_file="/shared/home/training_omat/test.xyz" \
--E0s='{8:-2049.91807262, 78: -518568.86288573, 22: -23328.13360429}' \
--forces_weight=100 \
--energy_weight=1 \
--energy_key='ref_energy' \
--forces_key='ref_forces' \
--lr=0.01 \
--scaling="rms_forces_scaling" \
--batch_size=4 \
--valid_batch_size=4 \
--max_num_epochs=200 \
--start_swa=300 \
--swa \
--swa_forces_weight=100 \
--ema \
--ema_decay=0.99 \
--pt_train_file="omat" \
--num_samples_pt 30000 \
--amsgrad \
--error_table='PerAtomMAE' \
--device='cuda' \
--distributed \
--default_dtype="float64" \
--seed=123 \
--restart_latest \
--save_cpu