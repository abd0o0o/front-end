from django.shortcuts import render

# Create your views here.
def base_page(request):
	return render(request,'forms/base.html')
def addDoctor_page(request):
	return render(request,'forms/add_doctor.html')
def addNurse_page (request):
    return render(request,'forms/add_nurse.html')
def addSpecialist(request):
    return render(request,'forms/specialist.html')
def addPharmacist(request):
    return render(request,'forms/add_pharmacist.html')
def addParamedic(request):
    return render(request,'forms/add_paramedic.html')
def addPatient(request):
    return render(request,'forms/add_patient.html')
def addstakeholders(request):
    return render(request,'forms/stakeholders.html')
def addMedicalInstitution(request):
    return render(request,'forms/add_medical_institutions.html')
def addInsuranceCompanies(request):
    return render(request,'forms/add_insurance_companies.html')
def addLab(request):
    return render(request,'forms/add_Lab.html')
def addClinic(request):
    return render(request,'forms/add_Clinic.html')
def addPharmacy(request):
    return render(request,'forms/add_Pharmacy.html')
def addHospital(request):
     return render(request,'forms/add_Hospital.html')
def addspecialization(request):
     return render(request,'forms/add_specialization.html')
def addpatient_history(request):
     return render(request,'forms/add_patient_history.html')
def add_Clinic_Work_Time(request):
     return render(request,'forms/add_Clinic_Work_Time.html')
def add_Hospital_Work_Time(request):
     return render(request,'forms/add_Hospital_Work_Time.html')
def addInsuranceType(request):
    return render(request,'forms/add_Insurance_Type.html')