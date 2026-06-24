import { writable } from 'svelte/store';

export const day = writable(1);
export const money = writable(50);
export const target: number = 50000;
export const values = writable<number[]>([]);
export const revenue = writable(0);
export const spending = writable(0);