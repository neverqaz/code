package h;

import javax.servlet.ServletRequestEvent;
import javax.servlet.ServletRequestListener;
import javax.servlet.annotation.WebListener;

/**
 * Application Lifecycle Listener implementation class AdressLisenter
 *
 */
@WebListener
public class AdressLisenter implements ServletRequestListener {

    /**
     * Default constructor. 
     */
    public AdressLisenter() {
        // TODO Auto-generated constructor stub
    }

	/**
     * @see ServletRequestListener#requestDestroyed(ServletRequestEvent)
     */
    public void requestDestroyed(ServletRequestEvent arg0)  { 
         // TODO Auto-generated method stub
    }

	/**
     * @see ServletRequestListener#requestInitialized(ServletRequestEvent)
     */
    public void requestInitialized(ServletRequestEvent arg0)  { //初始化
  
      //System.out.println(arg0.getServletRequest().getRemoteAddr());
    }
	
}
