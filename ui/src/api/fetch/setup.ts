import type { ExternalConfig } from "../types/externalConfig";
import ky from "ky";

export const fetchExternalConfig = async () => {
  try {
    return await ky
      .get(import.meta.env.BASE_URL + "externalConfig.json")
      .json<ExternalConfig>();
  } catch (error) {
    console.error(error);
    throw new Error("Cannot find external config");
  }
};
