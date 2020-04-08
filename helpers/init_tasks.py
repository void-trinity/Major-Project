import xml.etree.ElementTree as ET
from model.task import Task
from model.file import File

def init_tasks(filename):
    root = ET.parse(filename).getroot()
    tasks_dict = dict()

    for task in root.findall('./{http://pegasus.isi.edu/schema/DAX}job'):
        temp = Task(id = task.attrib['id'], runtime = float(task.attrib['runtime']))

        for file in task:
            if file.attrib['link'] == 'input':
                temp.add_input_file(File(name = file.attrib['file'], size = int(file.attrib['size'])))
            else:
                temp.add_output_file(File(name = file.attrib['file'], size = int(file.attrib['size'])))

        tasks_dict[temp.id] = temp

    for child in root.findall('./{http://pegasus.isi.edu/schema/DAX}child'):
        for parent in child:
            tasks_dict[child.attrib['ref']].add_predecessor_task(parent.attrib['ref'])
            tasks_dict[parent.attrib['ref']].add_successor_task(child.attrib['ref'])

    return tasks_dict
