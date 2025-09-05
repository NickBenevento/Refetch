import type { User } from "../../api/types/users";
import ky, { HTTPError } from "ky";
import { getExternalConfig } from "../../services/externalConfigService";

// TODO: Add toast notifications on error
export const fetchUsers = async (): Promise<User[]> => {
  const config = getExternalConfig();
  try {
    return await ky.get(`${config.apiService}/user/`).json<User[]>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error("HTTP error:", error.response.status);
    } else {
      console.error("Network or unexpected error:", error);
    }
    return [];
  }
};

export const createUser = async (): Promise<string | null> => {
  const config = getExternalConfig();
  try {
    return await ky.post(`${config.apiService}/user/${id}`).json<User>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error("HTTP error:", error.response.status);
    } else {
      console.error("Network or unexpected error:", error);
    }
    return null;
  }
};

export const fetchUserById = async (id: string): Promise<User | null> => {
  const config = getExternalConfig();
  try {
    return await ky.get(`${config.apiService}/user/${id}`).json<User>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error("HTTP error:", error.response.status);
    } else {
      console.error("Network or unexpected error:", error);
    }
    return null;
  }
};
