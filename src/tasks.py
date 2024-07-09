from crewai import Task
from textwrap import dedent

class EDA_Tasks:

    def ques_task(self,data_researcher):
        return Task(description=dedent("""
            You will create a list of questions to be answered in exploratory data analysis based on the data description:
			Data Description
			------------
        	{context}

			Your Final answer must be a list of 3 questions needed to be answered to gather meaningful insights, only the questions and nothing else.

            ###Question 1
            ###Question 2
            
            """),agent=data_researcher,expected_output="A list of questions")

    def ans_task(self,data_analyst):
        return Task(description=dedent("""
			You are helping in answering the question provided to you,
            
            Instructions to use the tool:

            1.Query should be passed in key value pair
            2. Key should be "input"
            3. Value should be the question
            
            These are the Question:
			Questions
			------------
            ###Question 1
            ###Question 2
            
			Using the tool available to you, you can answer to the question provided to you.
            Avoid irrelevant answers and do not provide any code in the answers.

			Your Final answer must be in the format given below:
            
            ###Question 1
            Answer
            ###Question 2 
            Answer
			"""),agent=data_analyst,expected_output="Answers to the question provided")

    def summarize_task(self,chief_da):
        return Task(description=dedent("""
				Write a 4-5 point data analysis report with covering all meaningful insights"""),agent=chief_da,expected_output="A report for the data analysis"
		)
