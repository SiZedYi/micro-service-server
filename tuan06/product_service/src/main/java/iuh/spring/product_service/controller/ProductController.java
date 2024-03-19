package iuh.spring.product_service.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class ProductController {
	@GetMapping("/product")
	public String getProduct() {
		return "get dc product";
	}
}
