# data_handler.py
# This script will handle functions related to saving and loading data
#
#=======================================================================================

import json
from datetime import date, time

def save_patient_info(patient_name, patient_id, dob, gender,
                      contact_number, email, visit_date, visit_time,
                      occupation, height_ft, height_in, weight_lbs,
                      emergency_name, emergency_relation, emergency_number,
                      medical_history, current_medications, allergies,
                      exercise_frequency, exercise_types, sleep_hours, stress_level,
                      previous_chiro,
                      primary_complaint, pain_onset, pain_cause,
                      pain_intensity_sharp, pain_intensity_shooting, pain_intensity_aching,
                      pain_intensity_burning, pain_intensity_tingling, pain_intensity_numbness,
                      pain_freq_sharp, pain_freq_shooting, pain_freq_aching,
                      pain_freq_burning, pain_freq_tingling, pain_freq_numbness,
                      consent, privacy_agreement):
    
    patient_data = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "dob": dob.isoformat() if isinstance(dob, date) else dob,
        "gender": gender,
        "contact_number": contact_number,
        "email": email,
        "visit_date": visit_date.isoformat() if isinstance(visit_date, date) else visit_date,
        "visit_time": visit_time.isoformat() if isinstance(visit_time, time) else visit_time,
        "occupation": occupation,
        "height_ft": height_ft,
        "height_in": height_in, 
        "weight_lbs": weight_lbs,
        "emergency_name": emergency_name,
        "emergency_relation": emergency_relation,
        "emergency_number": emergency_number,
        "medical_history": medical_history,
        "current_medications": current_medications,
        "allergies": allergies,
        "exercise_frequency": exercise_frequency,
        "exercise_types": exercise_types,
        "sleep_hours": sleep_hours,
        "stress_level": stress_level,
        "previous_chiro": previous_chiro,
        "primary_complaint": primary_complaint,
        "pain_onset": pain_onset.isoformat() if isinstance(pain_onset, date) else pain_onset, 
        "pain_cause": pain_cause,
        "pain_characteristics": {
            "sharp": {"intensity": pain_intensity_sharp, "frequency": pain_freq_sharp},
            "shooting": {"intensity": pain_intensity_shooting, "frequency": pain_freq_shooting},
            "aching": {"intensity": pain_intensity_aching, "frequency": pain_freq_aching},
            "burning": {"intensity": pain_intensity_burning, "frequency": pain_freq_burning},
            "tingling": {"intensity": pain_intensity_tingling, "frequency": pain_freq_tingling},
            "numbness": {"intensity": pain_intensity_numbness, "frequency": pain_freq_numbness}
            },
        "consent": consent,
        "privacy_agreement": privacy_agreement
    }

    with open(f"./data/patient_info_{patient_id}.json", "w") as f:
        json.dump(patient_data, f, indent=4)

def save_soap_info(patient_id, visit_date, chief_complaint, pain_location, pain_characteristics, pain_level,
                   pain_frequency, aggravating_factors, relieving_factors, affected_activities,
                   associated_symptoms,
                   vital_signs, blood_pressure, heart_rate, respiratory_rate,
                   temperature, height_ft, height_in, weight_lbs,
                   cervical_spine_flexion, cervical_spine_extension,
                   thoracic_spine_flexion, thoracic_spine_extension,
                   lumbar_spine_flexion, lumbar_spine_extension,
                   shoulders_flexion, shoulders_extension,
                   hips_flexion, hips_extension,
                   ortho_straight_leg_raise, ortho_kernig_sign, ortho_brudzinski_sign,
                   ortho_spurling_test, ortho_valsalva_maneuver,
                   neuro_deep_tendon_reflexes, neuro_muscle_strength, neuro_sensation,
                   palpation,
                   diagnosis, differential_diagnosis, prognosis,
                   treatment_provided, treatment_frequency, treatment_duration,
                   home_care_instructions, follow_up, referrals):

    soap_data = {
        "patient_id": patient_id,
        "visit_date": visit_date.isoformat() if isinstance(visit_date, date) else visit_date,
        "chief_complaint": chief_complaint,
        "pain_location": pain_location,
        "pain_characteristics": pain_characteristics,
        "pain_level": pain_level,
        "pain_frequency": pain_frequency,
        "aggravating_factors": aggravating_factors,
        "relieving_factors": relieving_factors,
        "affected_activities": affected_activities,
        "associated_symptoms": associated_symptoms,
        "vital_signs": vital_signs,
        "blood_pressure": blood_pressure,
        "heart_rate": heart_rate,
        "respiratory_rate": respiratory_rate,
        "temperature": temperature,
        "height_ft": height_ft,
        "height_in": height_in,
        "weight_lbs": weight_lbs,
        "cervical_spine_flexion": cervical_spine_flexion,
        "cervical_spine_extension": cervical_spine_extension,
        "thoracic_spine_flexion": thoracic_spine_flexion,
        "thoracic_spine_extension": thoracic_spine_extension,
        "lumbar_spine_flexion": lumbar_spine_flexion,
        "lumbar_spine_extension": lumbar_spine_extension,
        "shoulders_flexion": shoulders_flexion,
        "shoulders_extension": shoulders_extension,
        "hips_flexion": hips_flexion,
        "hips_extension": hips_extension,
        "ortho_straight_leg_raise": ortho_straight_leg_raise,
        "ortho_kernig_sign": ortho_kernig_sign,
        "ortho_brudzinski_sign": ortho_brudzinski_sign,
        "ortho_spurling_test": ortho_spurling_test,
        "ortho_valsalva_maneuver": ortho_valsalva_maneuver,
        "neuro_deep_tendon_reflexes": neuro_deep_tendon_reflexes,
        "neuro_muscle_strength": neuro_muscle_strength,
        "neuro_sensation": neuro_sensation,
        "palpation": palpation,
        "diagnosis": diagnosis,
        "differential_diagnosis": differential_diagnosis,
        "prognosis": prognosis,
        "treatment_provided": treatment_provided,
        "treatment_frequency": treatment_frequency,
        "treatment_duration": treatment_duration,
        "home_care_instructions": home_care_instructions,
        "follow_up": follow_up.isoformat() if isinstance(follow_up, date) else follow_up,
        "referrals": referrals
    }

    with open(f"./data/soap_notes_{patient_id}_{visit_date.strftime('%y%m%d')}.json", "w") as f:
        json.dump(soap_data, f, indent=4)
        
def save_treatment_plan_info(patient_name, patient_id, diagnosis,
                             plan_start_date, plan_duration,
                             initial_phase, maintenance_phase,
                             treatment_modalities,
                             chiro_techniques,
                             treatment_areas,
                             exercises, exercise_frequency,
                             home_care,
                             short_term_goals, long_term_goals,
                             outcome_measures,
                             precautions,
                             lifestyle_changes,
                             referrals,
                             reevaluation_frequency,
                             informed_consent):
    
    treatment_plan_data = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "diagnosis": diagnosis,
        "plan_start_date": plan_start_date.isoformat() if isinstance(plan_start_date, date) else plan_start_date,
        "plan_duration": plan_duration,
        "initial_phase": initial_phase,
        "maintenance_phase": maintenance_phase,
        "treatment_modalities": treatment_modalities,
        "chiro_techniques": chiro_techniques,
        "treatment_areas": treatment_areas,
        "exercises": exercises,
        "exercise_frequency": exercise_frequency,
        "home_care": home_care,
        "short_term_goals": short_term_goals,
        "long_term_goals": long_term_goals,
        "outcome_measures": outcome_measures,
        "precautions": precautions,
        "lifestyle_changes": lifestyle_changes,
        "referrals": referrals,
        "reevaluation_frequency": reevaluation_frequency,
        "informed_consent": informed_consent
    }

    with open(f"./data/treatment_plan_{patient_id}_{plan_start_date.strftime('%Y%m%d')}.json", "w") as f:
        json.dump(treatment_plan_data, f, indent=4)



    
    
