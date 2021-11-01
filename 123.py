import csv
def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines

def write_csv(file_name, data_list):
    with open(file_name, "w", newline="") as f:
        csv.writer(f).writerows(data_list)

def deal_data(arr):
    average_score = [["name", "avg"]]
    for i in range(1, len(arr)):
        score = arr[i].strip().split(",")
        average_score.append([score[0], (float(score[1])+ float(score[2]))/2])
    return average_score

def main():
  data = read_csv("practice.csv")
  result = deal_data(data)
  write_csv("result1.csv", result)
  print("--END--")

if __name__ == '__main__':
  main()