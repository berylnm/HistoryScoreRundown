# author: Binyi Wu

import csv
import sys

def file_length(filename):
	with open(filename, 'r', newline='', encoding='latin-1') as f:
		data = csv.DictReader(f)

		sum = 0
		for row in data:
			if (row['course']):
				sum += 1
			else:
				break
		return sum

def main():

	filename = sys.argv[1]
	outputname = sys.argv[2]

	sum = file_length(filename)
	rows = [[] for _ in range(sum)]

	with open(filename, 'r', newline='', encoding='latin-1') as f:
		data = csv.DictReader(f)
		
		i = 0

		for row in data:
			if (row['course']):
				course_info = row['course'].split(' ')

				quarter = course_info[0]
				if '"' in quarter:
					quarter = quarter[1:]
				if ':' in quarter:
					quarter = quarter[:len(quarter)-1]
				coursenum = course_info[2]
				coursetype = course_info[3]
				index = -1
				name = ""
				coursename = ""
				dis_num = ""
				for j in range(0, len(course_info)):
					if ',' in course_info[j]:
						index = j
						name = ' '.join(course_info[k] for k in range(j, len(course_info)-1))
						coursename = ''.join(course_info[k] for k in range(5, j))
					if 'DIS' in course_info[j]:
						dis_num = course_info[j+1].replace(':', '')		
				rows[i].append([name, quarter, coursenum, dis_num, coursetype, coursename])

			
			if (row['response']):
				response_info = row['response'].split(' ')
				for j in range(0, len(response_info)):
					if 'responses' in response_info[j]:
						rows[i][0].append(response_info[j+1])
						continue

					if 'Enrollment' in response_info[j]:
						rows[i][0].append(response_info[j+1])
						continue

					if 'Rate' in response_info[j]:
						rows[i][0].append(response_info[j+1])
						continue

			if (row['average']):
				average_info = row['average'].split(' ')
				for j in range(0, len(average_info)):
					if 'av' in average_info[j]:
						s = average_info[j]
						rows[i//2][0].append(s.replace('av.=', ''))

			i = i + 1
					

	with open(outputname, 'w', newline='', encoding='latin-1') as o:
		writer = csv.writer(o)
		for row in rows:
			writer.writerows(row)


if __name__== "__main__":
  main()
