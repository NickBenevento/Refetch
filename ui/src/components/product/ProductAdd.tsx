import ky from "ky";
import { useState } from "react";
import { getExternalConfig } from "../../services/externalConfigService";
import { fetchProducts } from "../../api/fetch/product";
import { useSetAtom } from "jotai";
import { productAtom } from "../../api/types/products";


const AddProduct = () => {
  const updateProducts = useSetAtom(productAtom);

  const config = getExternalConfig();
  const [formData, setFormData] = useState({
    name: "",
    url: "",
  });

  const addProduct = async (data: { name: string; url: string }) => {
    console.log("adding product: ", data);
    try {
      const response = await ky.post(`${config.apiService}/product/`, {
        json: data,
      });
      console.log("response: ", response);
      if (response.ok) {
        console.log("Product added successfully");
        if (response.ok) {
          console.log("Product added successfully");
          updateProducts(await fetchProducts());
        }
      }
    } catch (error) {
      console.error("Error adding product:", error);
    }
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();
    addProduct(formData);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Product name:
          <input
            className="bg-gray-200 text-black"
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </label>
        <label>
          Product URL:
          <input
            className="bg-gray-200 text-black"
            type="text"
            name="url"
            value={formData.url}
            onChange={handleChange}
          />
        </label>
        <button>Add Product</button>
      </form>
    </div>
  );
};

export default AddProduct;
