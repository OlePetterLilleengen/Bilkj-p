def beregn_bilkostnader(km_per_aar):
    # Definere konstanter for kostnader og priser
    forsikring_elbil = 5000  # kr/år for elbil
    forsikring_bensinbil = 7500  # kr/år for bensinbil
    trafikkforsikringsavgift_dag = 8.38  # kr/dag
    dager_i_året = 365  # antall dager i et år

    # Kostnader per kilometer
    forbruk_elbil_kwh_per_km = 0.2  # kWh per km for elbil
    strompris_per_kwh = 2.00  # kr per kWh
    forbruk_bensinbil_kr_per_km = 1.0  # kr per km for bensin
    bomavgift_elbil_per_km = 0.1  # kr per km for elbil
    bomavgift_bensinbil_per_km = 0.3  # kr per km for bensin

    # Beregning av totale årlige kostnader
    trafikkforsikringsavgift_aar = trafikkforsikringsavgift_dag * dager_i_året
    kostnad_elbil_drivstoff = forbruk_elbil_kwh_per_km * km_per_aar * strompris_per_kwh
    kostnad_elbil_bom = bomavgift_elbil_per_km * km_per_aar
    total_kostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_aar + kostnad_elbil_drivstoff + kostnad_elbil_bom

    kostnad_bensinbil_drivstoff = forbruk_bensinbil_kr_per_km * km_per_aar
    kostnad_bensinbil_bom = bomavgift_bensinbil_per_km * km_per_aar
    total_kostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_aar + kostnad_bensinbil_drivstoff + kostnad_bensinbil_bom

    # Beregning av årlig kostnadsdifferanse
    aarlig_kostnadsdifferanse = total_kostnad_bensinbil - total_kostnad_elbil

    # Skriv ut resultater
    print(f"Årlige totalkostnader for elbil: {total_kostnad_elbil:.2f} kr")
    print(f"Årlige totalkostnader for bensinbil: {total_kostnad_bensinbil:.2f} kr")
    print(f"Årlig kostnadsdifferanse (bensinbil - elbil): {aarlig_kostnadsdifferanse:.2f} kr")

def main():
    while True:
        try:
            km_per_aar = int(input("Vennligst oppgi antall kilometer kjørt per år: "))
            if km_per_aar >= 0:
                break
            else:
                print("Vennligst oppgi et positivt tall.")
        except ValueError:
            print("Ugyldig inntasting, vennligst oppgi et heltall.")
    
    beregn_bilkostnader(km_per_aar)

if __name__ == "__main__":
    main()
