#Outer loop is for outer folder structure
for i in {01..31}
do
	cd $i
	for j in {00..23} #THis inner loop is for the folder within the outer folder
	do
		cd $j
		cat aws-waf-logs* | egrep -o '"clientIp": "[^"]*", "country": "[^"]*"' | grep -v '"country": "IN"' #View specific pattern named file within each folder. Also, grep some specific data
		cd ../
	done
	cd ../
done
