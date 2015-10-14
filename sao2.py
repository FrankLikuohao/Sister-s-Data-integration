import sys,os 

if len(sys.argv) < 2:  
    print ("This is the program to integrate the function f(time,value) when value > reference level and output the result file")
    print ("usage:sys.argv[0] input_filename reference_value")
    print ("ex:sys.argv[0] testfile 94.2")
    print ("Designed by Frank Li at Taipei 2015/10/13 frank.likuohao@gmail.com")  
    sys.exit()
    
if len(sys.argv) >= 2:     
	filename=sys.argv[1]
	outfilename= filename + "result.csv"
	target = open(outfilename, 'w')
	reference_value=94.2

if len(sys.argv) >= 3:
	reference_value=float(sys.argv[2])

#print (len(sys.argv) )
lines = tuple(open(filename, 'r'))

title_lines=1
skip_line = 3

total_record = len(lines)

row_values_begin=lines[skip_line ].split()
#print(row_values_begin)
row_values_end=lines[total_record - 1].split()
#print(row_values_end)
total_time=int(row_values_end[0])  - int(row_values_begin[0])		

hundredcut = int(len(lines) / 100)

print ("input file [%s]\nOutput file [%s] \nReference_value[%8.2f]\ntotal record [%d] total time[%d](sec)" % (filename,outfilename,reference_value,total_record,total_time));



delterm=" "
IntegratedValue=0


#for i in range(len(lines)-833117 + 4184 ):
for i in range(len(lines)- 1 ):
	if i < title_lines:
		if i == 0:
			title=lines[i].rstrip('\n')
			#print (title)
			title_str1,title_str2=title.split('\t',2)	
			iterms = "%s,%s,%s,<%02.3f,%s,%s\n"%(title_str1,title_str2,"y*dt",reference_value,"Intergrated Value","Intergrated Value/Total BedTime")
			target.write(iterms)
			unit="%s,%s,%s,%s,%s,%s\n"         %("(sec)","[%]","(%sec)","1/0","(%sec)","(%sec)")
			target.write(unit)
		else:
			target.write(lines[i])
	if i < skip_line:
		next
	else:
		#print precentage
		modnumber = i % hundredcut	
		if modnumber == 0 :
			percent = i / total_record * 100
			print ("[%02d%s]" %(percent,"%"),end="",flush=True)
		#print(lines[i])
		
		#get two record values
		row_values=lines[i].split()
		row_values_next=lines[i+1].split()
		
		t=int(row_values[0])
		#print(t)
		t1=int(row_values_next[0])
		#print(t1)
		y_value=float(row_values[1])
		#print(y_value)		
		#function(94.2-y)*dt
		yXdt=(reference_value - y_value) * (t1 - t)
		#print(yXdt)
		if y_value <  reference_value:
			flag = 1
			#print ("flag = 1")
		else:
			#print ("flag = 0")
			flag = 0
		IntegratedValue = IntegratedValue + yXdt * flag
		#print (summation)
		output_str = "%5d ,%8.3f, %8.4f, %d, %8.4f , %8.4e \n" % (t, y_value,yXdt,flag,IntegratedValue, IntegratedValue / total_time)
		#print (output_str)
		target.write(output_str)
 
print ("End processing,\nWe write result to file[%s]"% (outfilename))
target.close()

