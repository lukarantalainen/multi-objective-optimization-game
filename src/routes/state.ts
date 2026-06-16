import { writable } from 'svelte/store';

export const day = writable(1);
export const money = writable(50);
export const target: number = 500;
export const finished = writable(false);