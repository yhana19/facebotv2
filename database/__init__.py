import dataset

class Thread():
  def __init__(self, thread_id):
    self.connect = dataset.connect('sqlite:///database/threads.db')
    self.db = self.connect[thread_id]
  
  def insert(self, data):
    self.db.insert(data)
  
  def find(self, *_clause, **kwargs):
    return self.db.find(*_clause, **kwargs)
  
  def find_one(self, *arg, **kwarg):
    return self.db.find_one(*arg, **kwarg)
  
  def update(self, row, keys):
    self.db.update(row, keys)