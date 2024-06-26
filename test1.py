
#include <iostream>
#include <cstdlib> // For system("cls")
#include <conio.h>
#include <string>

using namespace std;

class Employee {
public:
    string name;
    string number;
    double salary;
    string employee_id;
    int cnic;
    Employee *prev;
    Employee *Next;

    Employee() {
        prev = NULL;
        Next = NULL;
    }

    Employee(string n, string nu, double salarys, string employee_ids, int cnics) {
        name = n;
        number = nu;
        salary = salarys;
        employee_id = employee_ids;
        cnic = cnics;
    }
};


class EmployeeManagement {
    Employee *first;
    Employee *last;

public:
    EmployeeManagement() {
        first = NULL;
        last = NULL;
    }

    void addEmployee(string name, string number, double salary, string employee_id, int cnic) {
        Employee *t = new Employee(name, number, salary, employee_id, cnic);
        if (first == NULL) {
            first = t;
            last = t;
        } else {
            last->Next = t;
            t->prev = last;
            last = t;
        }
    }

    double updateSalary(string name, double salary) {
        Employee *t = first;
        if (first == NULL) {
            return -1;
        } else {
            while (t != NULL) {
                if (t->name == name) {
                    double s = t->salary;
                    t->salary = salary;
                    return s;
                } else {
                    t = t->Next;
                }
            }
        }
        return -1;
    }

    Employee *searchEmployee(string employee_id) {
        Employee *t = first;
        if (first == NULL) {
            return NULL;
        } else {
            while (t != NULL) {
                if (t->employee_id == employee_id) {
                    return t;
                } else {
                    t = t->Next;
                }
            }
        }
        return NULL;
    }

bool deleteEmployee(string name) {
    if (first->name == name) {
        if (first == last) {
            first = NULL;
            last = NULL;
        } else {
            first = first->Next;
            first->prev = NULL;
        }
        return true;
    } else {
        Employee *t = first;
        while (t->Next) {
            if (t->Next->name == name) {
                if (t->Next == last) {
                    last = t;
                    delete t->Next;
                    t->Next = NULL;
                } else {
                    Employee *temp = t->Next;
                    t->Next = t->Next->Next;
                    t->Next->prev = t;
                    delete temp;
                }
                return true;
            }
            t = t->Next;
        }
    }
    return false;
}

void print() {
    Employee *t = first;
    if (first == NULL) {
        cout << "THERE IS NO DATA OF THE EMPLOYEE:" << endl;
    } else {
        while (t) {
            cout << "NAME :                " << t->name << endl;
            cout << "CONTACT :              " << t->number << endl;
            cout << "SALARY :                " << t->salary << endl;
            cout << "Employee-id :           " << t->employee_id << endl;
            cout << "CNIC :                  " << t->cnic << endl;
            t = t->Next;
            cout<<"---------------------------------------"<<endl;
            cout<<endl;
        }
    }
}
};

int main() {
    EmployeeManagement e;
    Employee *t;
    double db;
    string n, s, employee_id;
    double salary;
    int cnic;
    string st;
    int choice;
    bool b;

    system("cls");
    system("Color 3B");
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t*Welcome to Employee Management System*" << endl;
    getch();

    while (true) {
        system("cls");
        system("Color 03");
        cout << "PRESS 0  TO EXIT:" << endl;
        cout << "PRESS 1  TO ADD NEW Employee:" << endl;
        cout << "PRESS 2  TO DELETE AN EMPLOYEE:" << endl;
        cout << "PRESS 3  TO UPDATE SALARY OF EMPLOYEE:" << endl;
        cout << "PRESS 4  TO SEARCH THE EMPLOYEE:" << endl;
        cout << "PRESS 5  TO PRINT THE ALL EMPLOYEES:" << endl;
        cin >> choice;

        switch (choice) {
            case 0:
                cout << "PROGRAM HAS BEEN ENDED" << endl;
                exit(0);
            case 1:
                system("cls");
                system("Color 03");
                cout << "ENTER THE NAME OF NEW EMPLOYEE:" << endl;
                cin >> s;
                cout << "ENTER THE CONTACT OF : " << s << endl;
                cin >> n;
                cout << "ENTER THE SALARY OF THE EMPLOYEE: " << endl;
                cin >> salary;
                cout << "ENTER THE EMPLOYEE ID OF THE EMPLOYEE: " << endl;
                cin >> employee_id;
                cout << "ENTER THE CNIC OF THE EMPLOYEE: " << endl;
                cin >> cnic;
                e.addEmployee(s, n, salary, employee_id, cnic);
                cout << "EMPLOYEE ADDED SUCCESSFULLY" << endl;
                break;
            case 2:
                system("cls");
                system("Color 03");
                cout << "ENTER THE NAME OF CONTACT WHICH YOU WANT TO DELETE:" << endl;
                cin >> s;
                b = e.deleteEmployee(s);
                if (b) {
                    cout << "THE DATA OF EMPLOYEE: " << s << " DELETED SUCCESSFULLY" << endl;
                } else {
                    cout << "THERE IS NO EMPLOYEE WITH THE NAME: " << s << endl;
                }
                break;
            case 3:
                system("cls");
                system("Color 03");
                cout << "ENTER THE NAME OF EMPLOYEE WHOSE SALARY YOU WANT TO UPDATE:" << endl;
                cin >> s;
                cout << "ENTER THE NEW SALARY OF: " << s << endl;
                cin >> salary;
                db = e.updateSalary(s, salary);
                if (db != -1) {
                    cout << "SALARY UPDATED SUCCESSFULLY" << endl;
                } else {
                    cout << "THERE IS NO EMPLOYEE WITH THE NAME: " << s << endl;
                }
                break;
            case 4:
                system("cls");
                system("Color 03");
                cout << "ENTER THE EMPLOYEE ID OF EMPLOYEE YOU WANT TO SEARCH:" << endl;
                cin >> employee_id;
                t = e.searchEmployee(employee_id);
                if (t != NULL) {
                    cout << "NAME OF EMPLOYEE :           " << t->name << endl;
                    cout << "CONTACT OF EMPLOYEE :         " << t->number << endl;
                    cout << "SALARY OF EMPLOYEE :           " << t->salary << endl;
                    cout << "Employee-id OF EMPLOYEE :      " << t->employee_id << endl;
                    cout << "CNIC OF EMPLOYEE :             " << t->cnic << endl;
                } else {
                    cout << "THERE IS NO EMPLOYEE WITH THE EMPLOYEE ID OF: " << employee_id << endl;
                }
                break;
            case 5:
                system("cls");
                system("Color 03");
                e.print();
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
                break;
        }
        cout << "Press any key to continue...";
        getch(); // Wait for a key press
    }

    return 0;
}