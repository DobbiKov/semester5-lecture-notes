set table "main.pgf-plot.table"; set format "%.5f"
set format "%.7e";; set samples 200; set dummy x; plot [x=0:126] 0.016* exp(-((x-75)/25)**2);
