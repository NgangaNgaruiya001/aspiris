from django.db import models

# Create your models here.
from django.db import models

class SalesData(models.Model):
    # Document details
    ObjType = models.CharField(max_length=50)  # Not important, but included for exact match
    DocumentType = models.CharField(max_length=50)  # Invoice or Credit Note
    ItemCode = models.CharField(max_length=50)  # Product code
    Dscription = models.CharField(max_length=255)  # Product name
    Quantity = models.FloatField()  # Total quantity sold
    Price = models.FloatField()  # Product price
    LineTotal = models.FloatField()  # Revenue from the product
    TotalFrgn = models.CharField(max_length=50, default="None")  # Division (e.g., Gyn, Pain)
    ItmsGrpCod = models.CharField(max_length=50, blank=True, null=True)  # Not important
    ItmsGrpNam = models.CharField(max_length=100, blank=True, null=True)  # Not important
    LineSlpCode = models.CharField(max_length=50, blank=True, null=True)  # Not important
    LineSlpName = models.CharField(max_length=100, blank=True, null=True)  # Not important
    AcctCode = models.CharField(max_length=50, blank=True, null=True)  # Not important
    AcctName = models.CharField(max_length=100, blank=True, null=True)  # Not important
    GrssProfit = models.FloatField()  # CM value
    DocNum = models.CharField(max_length=20)  # Invoice number
    DocDate = models.DateField()  # Date of the transaction
    DocYear = models.IntegerField()  # Year of the transaction
    DocMonth = models.IntegerField()  # Month of the transaction
    Time = models.CharField(max_length=50, blank=True, null=True)  # Not important
    DTime = models.CharField(max_length=50, blank=True, null=True)  # Not important
    CardCode = models.CharField(max_length=50)  # Customer code
    CardName = models.CharField(max_length=255)  # Customer name
    BRANCH = models.CharField(max_length=100)  # Branch of the customer
    BusinessPartnerCity = models.CharField(max_length=100, blank=True, null=True)  # Not important
    BusinessPartnerGroupName = models.CharField(max_length=100, blank=True, null=True)  # Not important
    BusinessPartnerCountry = models.CharField(max_length=100, blank=True, null=True)  # Not important
    SalesType = models.CharField(max_length=50, blank=True, null=True)  # Not important
    BuildingLocation = models.CharField(max_length=100)  # Building where product was made
    Department = models.CharField(max_length=100)  # Product department (e.g., tablet, capsule)
    SHELF = models.CharField(max_length=50)  # Shelf life of the product
    GroupCategory = models.CharField(max_length=50, blank=True, null=True)  # Not important
    PackSize = models.CharField(max_length=50, blank=True, null=True)  # Not important
    Seriez = models.CharField(max_length=50, blank=True, null=True)  # Not important
    TherapeuticCategory = models.CharField(max_length=100, blank=True, null=True)  # Not important
    SALE_TYPE = models.CharField(max_length=50)  # Direct, apportioned, or claimed

    # Regional quantities
    QTY_Nairobi_A = models.FloatField(null=True)
    QTY_Nairobi_B = models.FloatField(null=True)
    QTY_Nakuru = models.FloatField(null=True)
    QTY_Nyeri = models.FloatField(null=True)
    QTY_Kisumu = models.FloatField(null=True)
    QTY_Eldoret = models.FloatField(null=True)
    QTY_Mombasa = models.FloatField(null=True)
    TOTAL_QTY = models.FloatField(null=True)
    status = models.CharField(max_length=50, blank=True, null=True)  # Status (not important)

    # Regional sales values
    SALE_VALUE_Nairobi_A = models.FloatField(default=0)
    SALE_VALUE_Nairobi_B = models.FloatField(default=0)
    SALE_VALUE_Nakuru = models.FloatField(default=0)
    SALE_VALUE_Nyeri = models.FloatField(default=0)
    SALE_VALUE_Kisumu = models.FloatField(default=0)
    SALE_VALUE_Eldoret = models.FloatField(default=0)
    SALE_VALUE_Mombasa = models.FloatField(default=0)
    TOTAL_SALE_VALUE = models.FloatField(default=0)
    status2 = models.CharField(max_length=50, blank=True, null=True)  # Not important

    # Regional CM values
    CM_VALUE_Nairobi_A = models.FloatField(default=0)
    CM_VALUE_Nairobi_B = models.FloatField(default=0)
    CM_VALUE_Nakuru = models.FloatField(default=0)
    CM_VALUE_Nyeri = models.FloatField(default=0)
    CM_VALUE_Kisumu = models.FloatField(default=0)
    CM_VALUE_Eldoret = models.FloatField(default=0)
    CM_VALUE_Mombasa = models.FloatField(default=0)
    TOTAL_CM_VALUE = models.FloatField(default=0)
    status3 = models.CharField(max_length=50, blank=True, null=True)  # Not important
    # Miscellaneous



    CODE = models.CharField(max_length=50, blank=True, null=True)  # Not important
    L4_CUSTOMERS = models.CharField(max_length=255, blank=True, null=True)  # Customer type (L4 or other)

    def __str__(self):
        return f"{self.DocNum} - {self.Dscription} ({self.CardName})"
from django.db import models

# Create your models here.

class SalesTarget(models.Model):
    Month = models.IntegerField()
    Sub_division = models.CharField(max_length=50)  # Subdivision (e.g., Cardio, Gyn, Pain)
    Region = models.CharField(max_length=50)  # Region (e.g., Nairobi A, Nairobi B, etc.)
    Sales = models.FloatField()  # Sales value for the specific sub-division and region
    Year = models.IntegerField(default=2024)
    
    def __str__(self):
        return f"{self.Region} - {self.Sub_division} - {self.Month}"

