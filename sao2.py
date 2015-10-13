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

print (len(sys.argv) )
lines = tuple(open(filename, 'r'))
total_record = len(lines)
hundredcut = int(len(lines) / 100)



print ("input file [%s]\nOutput file [%s] \nReference_value[%8.2f]\ntotal record [%d]" % (filename,outfilename,reference_value,total_record));

title_lines=3

determ=" "
summation=0
skip_line = 0

#for i in range(len(lines)-833117 + 4184 ):
for i in range(len(lines)- 1 ):
	if i < title_lines:
		if i == 0:
			iterms = "%s %s <%8.3f %s \n"%(lines[i].rstrip('\n'),"y*dt",reference_value,"summation")
			target.write(iterms)
		else:
			target.write(lines[i])
	#if i <= skip_line:
	#	next
	else:
		
		modnumber = i % hundredcut	
		if modnumber == 0 :
			percent = i / total_record * 100
			print ("[%s%02d]" %("%",percent),end="",flush=True)
		#print(lines[i])
		row_values=lines[i].split()
		row_values_next=lines[i+1].split()
		
		t=int(row_values[0])
		#print(t)
		t1=int(row_values_next[0])
		#print(t1)
		y_value=float(row_values[1])
		#print(y_value)		
		yXdt=y_value * (t1 - t)
		#print(yXdt)
		if y_value <  reference_value:
			flag = 1
			#print ("flag = 1")
		else:
			#print ("flag = 0")
			flag = 0
		summation = summation + yXdt * flag
		#print (summation)
		output_str = "%5d %8.3f %8.3f %d %8.3f \n" % (t, y_value,yXdt,flag,summation)
		#print (output_str)
		target.write(output_str)
 
print ("End processing,\nWe write result to file[%s]"% (outfilename))
target.close()

