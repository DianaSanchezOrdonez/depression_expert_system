import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_rules_fn():
  engine.reset()
  engine.activate("fc_rules")
  print("doing proof")

  try:
    with engine.prove_goal("facts.depressed_total_score($name_patient, $total_score)") as gen:
      for vars, plan in gen:
        # Accede a las variables de la regla correctamente
        name_patient = vars['name_patient']
        total_score = vars['total_score']
        print("Dear", name_patient, "-", total_score)
  except Exception as e:
    print("Error:", e)
    krb_traceback.print_exc()
    sys.exit(1)

def fc_questions_fn():
  engine.reset()
  engine.activate("fc_questions_rules")
  print("doing proof")

  try:
    with engine.prove_goal("facts.depression_severity($total_score, $severity)") as gen:
      for vars, plan in gen:
        # Accede a las variables de la regla correctamente
        name_patient = vars['total_score']
        total_score = vars['severity']
        print("Dear", name_patient, "-", total_score)
  except Exception as e:
    print("Error:", e)
    krb_traceback.print_exc()
    sys.exit(1)

if __name__ == "__main__":
    fc_rules_fn()