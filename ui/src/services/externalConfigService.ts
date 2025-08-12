import type { ExternalConfig } from "../api/types/externalConfig";

export const setExternalConfig = (externalConfig: ExternalConfig) => {
  (window as any).__externalConfig__ = externalConfig;
};

export const hasExternalConfig = () => {
  return Boolean((window as any).__externalConfig__);
};

export const getExternalConfig = (): ExternalConfig => {
  const externalConfig = (window as any)
    .__externalConfig__ as unknown as ExternalConfig;
  if (!externalConfig) {
    throw Error("No external config found");
  }
  return externalConfig;
};
