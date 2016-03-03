Is Filled [![Build Status](https://travis-ci.org/futurice/isfilled.svg?branch=master)](https://travis-ci.org/futurice/isfilled)
============

Create rules for Models and ModelForms filledness.

Models validate while ModelForms present use-cases. Fills give insight on Model/ModelForm fields.

Why?
----

People are interested in different details. Create rules to accomodate each. Best used together with [On Condition](https://github.com/futurice/oncondition)
to send notifications on fill completions.

Usage
-----

Create a Model, which inherits `FillsMixin`. If you have a ModelForm, then adding a Fills checks the fields of the Form instead of the Model.

```python
class Employee(models.Model, FillsMixin):
    name = models.CharField(max_length=255)
    expert_in = models.CharField(max_length=255, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    editor_of_choice = models.CharField(max_length=255, blank=True, null=True)
    github_account = models.CharField(max_length=255, blank=True, null=True)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = []

class EmployeeSkillsForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['expert_in', 'editor_of_choice',]

class EmployeeFills(Filled):
    form = EmployeeForm

class EmployeeSkillsFills(Filled):
    form = EmployeeSkillsForm
```

Create Fills against Model:

```python
Fills.objects.create(name="employee-hr",
                     model="test.Employee",)

Fills.objects.create(name="employee-manager-bob",
                     model="test.Employee",
                     fields="starting_date, expert_in",)
```

Create Fills against ModelForm:

```python
Fills.objects.create(name="employee-hr",
                     fill="test.test_fills.EmployeeFills",)

Fills.objects.create(name="employee-team",
                     fill="test.test_fills.EmployeeSkillsFills",)
```

Filledness status:

```python
instance = Employee.objects.get(pk=1))
all_fills_filled, contexts = instance.check_fills()
```


