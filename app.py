from flask import Flask, json
from employee import Employee
import names

app = Flask(__name__)


@app.route("/getEmployeeList")
def getEmployeeList():
    try:

        # Initialize a employee list
        employeeList = []

        # create a instances for filling up employee list
        for i in range(0, 5):
            employee = Employee(names.get_first_name(), names.get_last_name())
            employeeList.append(employee)

        # convert to json data
        jsonStr = json.dumps([e.toJSON() for e in employeeList])

    except:
        print("error ", sys.exc_info()[0])

    return jsonStr


if __name__ == "__main__":
    app.run()
