# Use Google Sheet to collect data
  Lab from [lesson 7](https://github.com/kevinwlu/iot/tree/master/lesson7).
## Output and result
![](https://github.com/Gry1995/Iot-Project/blob/master/Use%20Google%20Sheet%20to%20collect%20data/IMG_3193.jpg)
![](https://github.com/Gry1995/Iot-Project/blob/master/Use%20Google%20Sheet%20to%20collect%20data/result.PNG)
## Try to collect more data
  We can find the key files are `system_info.py` and `rpi_spreadsheet.py`. Define `get functions` in `system_info.py` and use them in `rpi_spreadsheet.py` can help us collect more data.
  
  Also sheet printing function need to be extended:
  ```python
  worksheet.append_row((str(dat), cpu, tmp, XXX))
  ```
## Example
1. 
2.
3.
