package seleniumPractice;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class LaunchApp {

	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://ultimateqa.com/complicated-page#");
		driver.findElement(By.xpath("(//a[text()='Education'])[1]")).click();
		List<WebElement> links = driver.findElements(By.cssSelector("nav.et-menu-nav a"));
		WebElement seleniumResourcesLink = links.stream().filter(link -> link.getText().equals("Selenium Resources")).findFirst().orElse(null);
		seleniumResourcesLink.click();
		String title = driver.findElement(By.cssSelector("h1.entry-title")).getText();
		System.out.println(title);
		driver.quit();
	}

}
