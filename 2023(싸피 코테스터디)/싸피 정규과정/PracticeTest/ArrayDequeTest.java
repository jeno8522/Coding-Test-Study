package com.ssafy.temporary;

import java.util.ArrayDeque;
import java.util.Deque;

public class ArrayDequeTest {
	public static void main(String[] args) {
		Deque<Integer> d = new ArrayDeque<Integer>();
		d.addFirst(1);
		d.addLast(2);
		d.addFirst(3);
		System.out.println(d.toString());
		d.pollLast();
		System.out.println(d.toString());
		
		
	}
}
