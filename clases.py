
class Info():
  def __init__(self):
      self.paises = [
        "CHL",
        "PER",
        "BRA",
        "ECU",
        "BOL",
        "ARG"
      ]
      self.indicadores_gho = [
        "Number of deaths", "Number of infant deaths", "Number of under-five deaths", 
        "Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)",
        "Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)",
        "Estimates of rates of homicides per 100 000 population",
        "Crude suicide rates (per 100 000 population)",
        "Mortality rate attributed to unintentional poisoning (per 100 000 population)",
        "Number of deaths attributed to non-communicable diseases, by type of disease and sex",
        "Estimated road traffic death rate (per 100 000 population)",
        "Estimated number of road traffic deaths",
        "Mean BMI (kg/m&#xb2;) (crude estimate)",
        "Mean BMI (kg/m&#xb2;) (age-standardized estimate)",
        "Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%)",
        "Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)",
        "Prevalence of overweight among adults, BMI &GreaterEqual; 25 (crude estimate) (%)",
        "Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)",
        "Prevalence of underweight among adults, BMI < 18.5 (crude estimate) (%)",
        "Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)",
        "Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)",
        "Estimate of daily cigarette smoking prevalence (%)",
        "Estimate of daily tobacco smoking prevalence (%)",
        "Estimate of current cigarette smoking prevalence (%)",
        "Estimate of current tobacco smoking prevalence (%)",
        "Mean systolic blood pressure (crude estimate)",
        "Mean fasting blood glucose (mmol/l) (crude estimate)",
        "Mean Total Cholesterol (crude estimate)"
      ]
      self.dict = {
        "GHO": [],
        "COUNTRY": [],
        "SEX": [],
        "YEAR": [],
        "GHECAUSES": [],
        "AGEGROUP": [],
        "Display": [],
        "Numeric": [],
        "Low": [],
        "High": []
      }

