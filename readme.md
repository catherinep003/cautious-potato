# cautious-potato
Simple script to automatically generate text files containing student grades from a CSV file. Each text file is added to the respective student assignment file submission directory.

## Assignment Directory Format
The following format indicates the assignment folder in which the student assignment submissions can be found that must be copied/moved to the `resources` folder.

```
assignmentRoot\
  [course]\
    [student]\
      [assignment]\
        [submissionTimestamp]
```

**Student Folder Name Format Example**  
`12345678-user_name` where `12345678` is the student ID

**Submission Timestamp Folder Name Format Example**  
`2016-Feb-4-16h56m4s762ms`

## CSV File Format
Please note that it is important to follow the CSV file format shown below for the best results.

Student ID | Grade 1 (/X) | Grade n (/X) | Total (/X) | Notes
-----------|--------------|--------------|------------|------
12345678 | 1 | ... | 20 |

## Mark File Format
Student ID: 12345678  
Grade 1 (/X): 1  
...  
Total (/X): 20  
Notes:  

## Instructions
1. There should be a 'resources' folder that contains:
  * the CSV file that contains all the grades
  * and the folder containing all the assignments of the students
2. Open command prompt or terminal
3. Navigate to the script directory  
  e.g. `cd \cautious-potato\src`
4. Run
  * `main.py` or
  * `python main.py`
3. As indicated by the prompt that will show up, enter the CSV file name that resides in the `resources` folder.
4. Again, as prompted, enter the folder name that contains the students' submissions.
5. Tada~ There will be a message indicating which students had a mark file generated and the total number, for your information.
