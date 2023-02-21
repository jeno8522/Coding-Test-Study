package com.ssafy.algorithm.BOJ;

import java.util.Scanner;

public class Main_1244_S4_스위치켜고끄기_주창훈 {
    static int n;
    static int m;
    static int[] arr;

public static void flipMultiple(int num) {
    for (int i = num - 1; i < n; i += num) {
        if (arr[i] == 0)
            arr[i] = 1;
        else
            arr[i] = 0;
    }
}

public static void flipSymmetry(int cnt) {
	int num = cnt - 1;
    if (arr[num] == 0)
        arr[num] = 1;
    else
        arr[num] = 0;
    int i = 1;
    while(num - i >= 0 && num + i < n) {
        if (arr[num - i] == arr[num + i]) {
            if (arr[num - i] == 0) {
                arr[num - i] = 1;
                arr[num + i] = 1;
            } else {
                arr[num - i] = 0;
                arr[num + i] = 0;
            }
        } else {
            break;
        }
        i++;
    }
}


// 백준 15650  N과 M
//BJ15560_이름1_이름2.pdf

public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = sc.nextInt();
    }
    m = sc.nextInt();
    int[][] command = new int[m][2];
    for (int i = 0; i < m; i++) {
        command[i][0] = sc.nextInt();
        command[i][1] = sc.nextInt();
    }
    for (int i = 0; i < m; i++) {
        if (command[i][0] == 1) {
            flipMultiple(command[i][1]);
//            for (int e : arr) {
//                System.out.print(e + " ");
//            }
//            System.out.println();

        } else {
            flipSymmetry(command[i][1]);
//            for (int e : arr) {
//                System.out.print(e + " ");
//            }
//            System.out.println();
        }
    }
    
    int cnt = 0;
    
    for (int e : arr) {
        System.out.print(e + " ");
        cnt++;
        if(cnt == 20) {
        	System.out.println();
        	cnt = 0;
        }
    }

}
}