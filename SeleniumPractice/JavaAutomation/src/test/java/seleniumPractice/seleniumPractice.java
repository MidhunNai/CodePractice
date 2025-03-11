package seleniumPractice;

import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class seleniumPractice {
	
	WebDriver driver;
	
	@BeforeTest
	public void initiateBrowser() {
		driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://ultimateqa.com/complicated-page#");
	}
	
//	@Test //Test dropdown which appears on hover
//	public void launch(){
//		
//		driver.findElement(By.xpath("(//a[text()='Education'])[1]")).click();
//		List<WebElement> links = driver.findElements(By.cssSelector("nav.et-menu-nav a"));
//		WebElement seleniumResourceLink = links.stream().filter(link -> link.getText().equals("Selenium Resources")).findFirst().orElse(null);
//		seleniumResourceLink.click();
//		String title = driver.findElement(By.cssSelector("h1.entry-title")).getText();
//		System.out.println(title);
//		driver.quit();
//	}
	
//	@Test //Test content hide functionality
//	public void test2() {
//		List<WebElement> links = driver.findElements(By.tagName("a"));
//		WebElement hideButton = null;
//		for(WebElement link : links) {
//			if(link.getText().equals("hide")) {
//				hideButton = link;
//				break;
//			}
//		}
//		if(hideButton != null) {
//		((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", hideButton);
//		} else {
//			System.out.println("Hide button not found");
//		}
//		hideButton.click();
//		//driver.quit();
//	}
	
	@Test //Fill Form
	public void test3() {
		driver.findElement(By.xpath("//div[@id='et_pb_contact_form_0']//input[@placeholder='Name']")).sendKeys("Iris");
		driver.findElement(By.xpath("//div[@id='et_pb_contact_form_0']//input[@placeholder='Email Address']")).sendKeys("iris.nair@test.com");
		driver.findElement(By.xpath("//div[@id='et_pb_contact_form_0']//textarea[@placeholder='Message']")).sendKeys("Hello this is Iris from Kerala");
		String calculateText = driver.findElement(By.cssSelector("#et_pb_contact_form_0 p.clearfix span")).getText();
		System.out.println(calculateText);
		String[] textArr = calculateText.split("\\+");
		String sum =  String.valueOf(Integer.parseInt(textArr[0].trim()) + Integer.parseInt(textArr[1].trim()));
		System.out.println(sum);
		driver.findElement(By.xpath("//div[@id='et_pb_contact_form_0']//p[@class='clearfix']//input")).sendKeys(sum);
		driver.findElement(By.xpath("//div[@id='et_pb_contact_form_0']//button[@type='submit']")).click();
	}

}
