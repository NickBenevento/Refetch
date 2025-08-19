import ky from "ky";
import { useState } from "react";
import ProductList from "./ProductList";
import { getExternalConfig } from "../../services/externalConfigService";

const ProductsPage = () => {
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
          await fetchProducts(); // <-- refetch after adding
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
    console.log("Submitting product:", formData);
    addProduct(formData);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Our Products</h1>
      <ProductList />
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

export default ProductsPage;
