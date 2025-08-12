// import ReactDOM from "react-dom/client";
import { setExternalConfig } from "./services/externalConfigService";
import { fetchExternalConfig } from "./api/fetch/setup";
import type { ExternalConfig } from "./api/types/externalConfig";
// import { RouterProvider } from "react-router/dom";
// import { router } from "./router";

// const render = () => {
//   ReactDOM.createRoot(document.getElementById("root")!).render(
//     <RouterProvider router={router} />
//   );
// };

const init = async () => {
  // Fetch the external config before app launches
  let externalConfig: ExternalConfig;
  try {
    externalConfig = await fetchExternalConfig();
    setExternalConfig(externalConfig);
  } catch (error) {
    console.error(error);
    throw new Error("Cannot find external config");
  }

  // render();
};

void init();
