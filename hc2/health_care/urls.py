"""health_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from forms import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("base/", views.base_page),
    path("add_doctor/", views.addDoctor_page),
    path("add_nurse/",views.addNurse_page),
    path("add_specialist/",views.addSpecialist),
    path("add_pharmacist/",views.addPharmacist),
    path("add_paramedic/",views.addParamedic),
    path("add_patient/",views.addPatient),
    path("add_stakeholders/",views.addstakeholders),
    path("add_MI/",views.addMedicalInstitution),
    path("add_IC/",views.addInsuranceCompanies),
    path("add_Lab/",views.addLab) ,
    path("add_Clinic/",views.addClinic),
    path("add_Pharmacy/",views.addPharmacy),
    path("add_Hospital/",views.addHospital),
    path("add_Specialization/",views.addspecialization),
    path("add_pHistory/",views.addpatient_history),
    path("add_C_Work_Time/",views.add_Clinic_Work_Time),
    path("add_H_Work_Time/",views.add_Hospital_Work_Time),
    path("add_I_Type/",views.addInsuranceType)


]
