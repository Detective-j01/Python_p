#include <iostream>
#include <cstdlib>
using namespace std;

class Myclass1 {
private:
    int field1;
    int field2;
    int field3;
    const int constField;
    static int ID;

public:
    Myclass1() : field1(rand()), field2(rand()), field3(rand()), constField(0) {
        ID++;
    }

    Myclass1(int val1) : field1(val1), field2(rand()), field3(rand()), constField(0) {
        ID++;
    }

    Myclass1(int val1, int val2) : field1(val1), field2(val2), field3(rand()), constField(0) {
        ID++;
    }

    Myclass1(int val1, int val2, int val3) : field1(val1), field2(val2), field3(val3), constField(0) {
        ID++;
    }

    Myclass1(int val1, int val2, int val3, int val4) : field1(val1), field2(val2), field3(val3), constField(val4) {
        ID++;
    }

    void PrintDetails() {
        cout << "ID: " << ID << endl;
        cout << "Field1: " << field1 << endl;
        cout << "Field2: " << field2 << endl;
        cout << "Field3: " << field3 << endl;
        cout << "ConstField: " << constField << std::endl;
    }

    static Myclass1 ObjectCreate(const Myclass1& obj) {
        Myclass1 modifiedObj = obj;
        modifiedObj.field1 += 10;
        modifiedObj.field2 += 20;
        modifiedObj.field3 += 30;
        return modifiedObj;
    }
};

int Myclass1::ID = 0;

class Myclass2 {
private:
    int field1;
    int field2;
    int field3;
    const int constField;
    static int ID;

public:
    Myclass2() : field1(rand()), field2(rand()), field3(rand()), constField(0) {
        ID++;
    }

    void PrintDetails() {
        std::cout << "ID: " << ID << std::endl;
        std::cout << "Field1: " << field1 << std::endl;
        std::cout << "Field2: " << field2 << std::endl;
        std::cout << "Field3: " << field3 << std::endl;
        std::cout << "ConstField: " << constField << std::endl;
    }

};

int Myclass2::ID = 0;

class Myclass3 {
private:
    int field1;
    int field2;
    int field3;
    const int constField;
    static int ID;

public:
    Myclass3() : field1(rand()), field2(rand()), field3(rand()), constField(0) {
        ID++;
    }

    void PrintDetails() {
        std::cout << "ID: " << ID << std::endl;
        std::cout << "Field1: " << field1 << std::endl;
        std::cout << "Field2: " << field2 << std::endl;
        std::cout << "Field3: " << field3 << std::endl;
        std::cout << "ConstField: " << constField << std::endl;
    }

};

int Myclass3::ID = 0;

int main() {
 
    Myclass1 obj1;
    Myclass1 obj2(42);
    Myclass1 obj3(12, 34);
    Myclass1 obj4(1, 2, 3);
    Myclass1 obj5(5, 10, 15, 20);
    Myclass1 obj6(99, 88, 77, 66);


    obj1.PrintDetails();
    obj2.PrintDetails();
    obj3.PrintDetails();
    obj4.PrintDetails();
    obj5.PrintDetails();
    obj6.PrintDetails();

    return 0;
}

