from django.db import models


TYPES_OF_COMPLAINTS = (
    ('Traffic Violation', 'Traffic Violation'),
    ('Delayed Services', 'Delayed Services'),
    ('Service Quality', 'Service Quality'),
    ('Service Denial', 'Service Denial'),
    ('Missuse of Funds', 'Missuse of Funds'),
    ('Road and Transportatoin Issues', 'Road and Transportation Issues'),
    ('Healthcare Services', 'Healthcare Services'),
    ('Misconduct Allegations', 'Misconduct Allegations'),
    ('Abuse of Power', 'Abuse of Power'),
    ('Other', 'Other'),
)

class Complaint(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type_of_complaint = models.CharField(max_length=100, choices=TYPES_OF_COMPLAINTS)
    created_at = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    action_taken = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.description
    