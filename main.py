class job:
  salary = None
  name = None
  hours_worked = None
 
  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = salary
    self.hours_worked = hours_worked
    
  def detail(self):
    print((f"{self.name} has {self.salary} salary and works for {self.hours_worked} hours."))
    

class doctor(job):
  speciality = None
  yoe = None

  def __init__(self, salary, hours_worked, speciality, yoe):
      self.name = "Doctor"
      self.salary = salary
      self.hours_worked = hours_worked
      self.speciality = speciality
      self.yoe = yoe


  def detail(self):
    print((f"{self.name} who is specialist in {self.speciality} with experience of {self.yoe} years has {self.salary} salary and works for {self.hours_worked} hours."))

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hours_worked, subject, position):
      self.name = "Teacher"
      self.salary = salary
      self.hours_worked = hours_worked
      self.subject = subject
      self.position = position

   
  def detail(self):
    print((f"{self.name} who is {self.position} teaches {self.subject} and has {self.salary} salary and works for {self.hours_worked} hours."))

lawyer = job("Lawyer", "$100,000", "40")
lawyer.detail()
print()

doc = doctor("$120,000", "48","Pediatric Consultant", "7")
doc.detail()
print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.detail()




