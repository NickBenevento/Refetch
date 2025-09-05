import { atom } from "jotai";
export interface Product {
  id_: string;
  url: string;
  name: string;
}

export const productAtom = atom<Product[] | null>(null);
