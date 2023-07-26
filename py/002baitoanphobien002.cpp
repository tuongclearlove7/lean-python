#include<iostream>
using namespace std;

template <class p1, class p2>       //Khuôn mẫu hàm, và cho p1 là 1 kiểu dữ liệu chung
p1 Tinh_tong (p1, p2);               //Khai báo hàm
void Nhap_mang(int arr[], int );
void Xuat_mang(int arr[], int);
void Xuat_phantunguyento_mang(int arr[], int );
void Them1 (int arr[], int , int , int );

int main()
{
    int a[100];
    int n, x, k;
    cout << "\nNhap so luong phan tu mang: ";
    cin >> n;
    Nhap_mang(a, n);
    cout << "\nVi tri can them phan tu vao mang: ";//Them phan tu moi
    cin >> k;
    cout << "\nGia tri phan tu cam them vao mang: ";
    cin >> x;
    Them1(a, n, x, k);
    Xuat_mang(a, n);
    Xuat_phantunguyento_mang (a, n);
    system("pause");
    return 0;
}

template <class p1, class p2>          //Khuôn mẫu hàm
p1 Tinh_tong (p1 a, p2 b )
{
    return (a+b);
}

void Nhap_mang(int arr[], int n){       //Hàm nhập mảng
    for(int i=0; i<n;i++)
    {
        cout << "\nNhap phan tu arr[" << i << "] = ";
        cin >> arr[i] ;

    }
}

void Xuat_mang(int arr[], int n)        //Hàm xuất mảng
{
    cout << "\nGia tri cua mang lan luot la: ";
    for (int i=0; i<n; i++)
    {
        cout << arr[i] << " ";
    }
}

void Xuat_phantunguyento_mang (int arr[], int n)    //Hàm xuất các phần tử nguyên tố trong mảng
{
    cout << "\nCac so nguyen to la: ";
    for (int i=0; i<n; i++)
    {
        bool KT=true;
        if (arr[i]<2)
        {
            KT=false;
        }
        else
        {
            for (int j=2; j< arr[i]; j++)
            {
                if (arr[i]%j == 0)
                {
                    KT=false;
                    break;
                }
            }
        }
        if (KT== true)
        {
            cout << arr[i] << " ";
        }
        
    }
    system("pause");
}

void Them1(int arr[], int &n, int x, int k)    //Hàm có nhiệm vụ thêm 1 phần tử vào mảng
{
    for (int i=n-1; i>=k; i--)
    {
        arr[i+1] = arr[i];
    }
    arr[k]=x;
    n=n+1;
}


// #include<iostream>
// using namespace std;

// // nhập mảng
// void Nhap_Mang(int a[], int n)
// {
// 	for(int i = 0; i < n; i++)
// 	{
// 		cout << "\nNhap gia tri a[" << i << "]= ";
// 		cin >> a[i];
// 	}
// }

// // xuất mảng
// void Xuat_Mang(int a[], int n)
// {
// 	for(int i = 0; i < n; i++)
// 	{
// 		cout << a[i] << " ";
// 	}
// }

// // hàm có nhiệm vụ thêm 1 phần tử x vào vị trí k bất kì trong mảng
// void Them(int a[], int &n, int x, int k)
// {
// 	for(int i = n-1; i >= k; i--)
// 	{
// 		a[i+1] = a[i];
// 	}
// 	a[k] = x; // gán phần tử cần thêm x vào chính vị trí k
// 	n++; // số lượng phần tử mảng tăng lên 1 đơn vị
// }

// int main()
// {
// 	int a[100];
// 	int n;

// 	do
// 	{
// 		cout << "\nNhap so luong phan tu mang: ";
// 		cin >> n;
// 		if(n <= 0 || n > 100)
// 		{
// 			cout << "\nSo luong phan tu mang khong hop le";
// 			system("pause");
// 		}
// 	}while(n <= 0 || n > 100);

// 	cout << "\n\n\t\t NHAP MANG\n";
// 	Nhap_Mang(a, n);
// 	cout << "\n\n\t\t XUAT MANG\n";
// 	Xuat_Mang(a, n);

// 	int x; // giá trị cần thêm vào mảng
// 	cout << "\nNhap gia tri can them: ";
// 	cin >> x;
// 	int vitri;
// 	cout << "\nNhap vi tri can them: ";
// 	cin >> vitri;

// 	Them(a, n, x, vitri); // gọi lại hàm thêm để thêm 1 phần tử x vào vị trí 
// 	cout << "\n\n\t\t XUAT MANG SAU KHI THEM\n";
// 	Xuat_Mang(a, n);

// 	system("pause");
// 	return 0;
// }