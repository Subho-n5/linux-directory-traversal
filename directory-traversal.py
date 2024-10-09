for i in {01..31}
do
	cd $i
	for j in {00..23}
	do
		cd $j
		cat aws-waf-logs* | egrep -o '"clientIp": "[^"]*", "country": "[^"]*"' | grep -v '"country": "IN"'
		cd ../
	done
	cd ../
done
