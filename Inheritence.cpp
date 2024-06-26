#include<iostream>
using namespace std;
class Father{
		protected:
			string surname ="Kanwar";
};		
class Son1:Father{
	string name ="Muhammad Jawad";
	public: 
	void show(){
		 cout<<name<<" "<<surname<<endl;
	}
};
class Son2:Father{
	string name ="Ahmed Rafay";
	public: 
	void disp(){
		 cout<<name<<" "<<surname<<endl;
	}
};
int main(){
	Son1 s1;
	s1.show(); 
	
	Son2 s2;
	s2.disp();
}
