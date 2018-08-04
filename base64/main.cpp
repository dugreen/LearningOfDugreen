#include "iostream"
#include "string.h"

using namespace std;

void main(){
  string strData = "hello";
  //对straData进行Base64编码
  ZBase64 zBase;
  string strResult=zBase.Encode(buffer,size);
  cout<<strResult<<endl;
}
