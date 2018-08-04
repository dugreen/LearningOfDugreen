// ConsoleApplication.cpp: 定义控制台应用程序的入口点。
//
#include<iostream>
#include "stdafx.h"
#include "windows.h"
#include "string.h"
#include "ZBase64.h"

using namespace std;

int main()
{
	/*
	 *编码
	*/
	string strData = "hello";
	cout << "编码前:" <<strData<< endl;
	
	const unsigned char* temp = (const unsigned char*)strData.c_str();
	//unsigned char* pUC = const_cast<unsigned char*> (pCUC);
	//对straData进行Base64编码
	ZBase64 zBase;
	int size = strData.length();
	string strResult = zBase.Encode(temp, size);
	cout <<"编码后："<< strResult << endl;


	/*
	 * 解码
	*/
	string str_data = "aGVsbG8=";
	cout << "解码前:" << str_data << endl;

	const char* temp_s = (const char*)str_data.c_str();
	//unsigned char* pUC = const_cast<unsigned char*> (pCUC);

	int size_s = str_data.length();
	int outByte = 0;
	string strResult_s = zBase.Decode(temp_s, size_s,outByte);
	cout << "解码后：" << strResult_s << endl;
	Sleep(1000000000);
	
    return 0;
}


