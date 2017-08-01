from squad.demo_prepro import prepro
from basic.demo_cli import Demo
import argparse


parser = argparse.ArgumentParser(description='Run question answering program in interactive(default) or batch mode')
parser.add_argument('file', help='question file location')
args = parser.parse_args()

def get_answer(paragraph, question):
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro['x'])>1000:
        return "[Error] Sorry, the number of words in paragraph cannot be more than 1000." 
    if len(pq_prepro['q'])>100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    return demo.run(pq_prepro)

demo = Demo()

if __name__=='__main__':
    paragraph=""
    questions=[]
    print("Reading file ", args.file)
    with open(args.file, 'r') as q_file:
        for line in q_file:
            if line.strip()=='# QUESTIONS':
                break
            paragraph+= line
        for line in q_file:
            questions.append(line)
    for question in questions:
        print(get_answer(paragraph,question))
            





