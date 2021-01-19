### safety barrier - because generation already happened
#exit 1

rm -rf tasksgen
python3 multigen.py
cd ../pdfgen
rm -rf *-out
python3 gen.py
