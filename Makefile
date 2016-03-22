all:
	echo hi

preround1.trfx: pre_round_1_inputs.csv
	./csv_to_trfx.py pre_round_1_inputs.csv > preround1.trfx

round_1_results.csv: preround1.trfx
	./make_results.py pre_round_1_inputs.csv preround1.trfx \
round1.trfx round_1_results.csv 1

round1: round_1_results.csv



pre_round_2_inputs.csv:
	./combine_results_w_input.py \
pre_round_1_inputs.csv round_1_results.csv pre_round_2_inputs.csv

preround2: pre_round_2_inputs.csv

preround2.trfx: pre_round_2_inputs.csv
	./csv_to_trfx.py pre_round_2_inputs.csv > preround2.trfx

round_2_results.csv: preround2.trfx
	./make_results.py pre_round_2_inputs.csv preround2.trfx \
round2.trfx round_2_results.csv 2

round2: round_2_results.csv


pre_round_3_inputs.csv:
	./combine_results_w_input.py \
pre_round_2_inputs.csv round_2_results.csv pre_round_3_inputs.csv

preround3: pre_round_3_inputs.csv

preround3.trfx: pre_round_3_inputs.csv
	./csv_to_trfx.py pre_round_3_inputs.csv > preround3.trfx
round_3_results.csv: preround3.trfx
	./make_results.py pre_round_3_inputs.csv preround3.trfx \
round3.trfx round_3_results.csv 3

round3: round_3_results.csv


pre_round_4_inputs.csv:
	./combine_results_w_input.py \
pre_round_3_inputs.csv round_3_results.csv pre_round_4_inputs.csv

preround4: pre_round_4_inputs.csv

preround4.trfx: pre_round_4_inputs.csv
	./csv_to_trfx.py pre_round_4_inputs.csv > preround4.trfx
round_4_results.csv: preround4.trfx
	./make_results.py pre_round_4_inputs.csv preround4.trfx \
round4.trfx round_4_results.csv 4

round4: round_4_results.csv


pre_round_5_inputs.csv:
	./combine_results_w_input.py \
pre_round_4_inputs.csv round_4_results.csv pre_round_5_inputs.csv

preround5: pre_round_5_inputs.csv

preround5.trfx: pre_round_5_inputs.csv
	./csv_to_trfx.py pre_round_5_inputs.csv > preround5.trfx
round_5_results.csv: preround5.trfx
	./make_results.py pre_round_5_inputs.csv preround5.trfx \
round5.trfx round_5_results.csv 5

round5: round_5_results.csv

