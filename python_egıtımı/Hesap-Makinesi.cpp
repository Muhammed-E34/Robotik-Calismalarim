#include <iostream>
using namespace std;

int main() {
    int x,y,sonuc;

    cout<<"Birinci sayıyı giriniz:";
    cin>>x;

    cout<<"ikinci sayıyı giriniz: ";
    cin>>y;

    if (x>y) {

        sonuc= x*y;
        cout<<"sonuç (carpma):"<< sonuc << endl;

}
else {
    sonuc=x+y;
    cout<< "sonuç (toplama):" << sonuc << endl;
}

return 0
}
  