import type { Product } from "../../api/types/products";
import ky, { HTTPError } from "ky";
import { getExternalConfig } from "../../services/externalConfigService";

export const fetchProducts = async (): Promise<Product[]> => {
  const config = getExternalConfig();
  try {
    return await ky.get(`${config.apiService}/product/`).json<Product[]>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error("HTTP error:", error.response.status);
    } else {
      console.error("Network or unexpected error:", error);
    }
    return [];
  }
};
