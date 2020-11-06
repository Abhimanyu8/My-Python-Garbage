
#include <iostream>
using namespace std;
int main()
{ 
int girlfriend;
cout<< "How many girlfriend(s) do you want" <<  endl;
cin >> girlfriend;
 
do 
{ cout <<"Okay I'll give you" << girlfriend << "but pay me first\n";
}
while (girlfriend !=0);
return 0;
}
