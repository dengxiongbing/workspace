/*
 * Copyright 2010 Google Inc.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package com.google.jstestdriver.server.handlers;

import com.google.inject.Inject;
import com.google.inject.servlet.RequestParameters;
import com.google.jstestdriver.requesthandlers.RequestHandler;

import org.mortbay.jetty.MimeTypes;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.lang.Exception;
import java.lang.InterruptedException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;

import javax.servlet.http.HttpServletResponse;

/**
 * Used by the client to sleep milliSeconds time
 * @author xiaodeng
 * @Time  /09/21/2012
 */
class ApiHandler implements RequestHandler {

  private static final Logger LOGGER = LoggerFactory.getLogger(
      ApiHandler.class);

  private final Map<String, String[]> parameters;
  private final HttpServletResponse response;

  @Inject
  public ApiHandler(
      @RequestParameters Map<String, String[]> parameters,
      HttpServletResponse response) {
      this.parameters = parameters;
      this.response = response;
  }
  
  public String mySleep(String milliSecond)
  {
	  String sMsg = "OK";
	  int nMilliSecond = -1;
      try {
   	      if (null != milliSecond) {
              nMilliSecond = Integer.parseInt(milliSecond, 10);
    	  }
   	      else {
              sMsg = "milliSecond is null";
   	      }
      } catch (Exception e) {
          sMsg = e.toString();
          LOGGER.debug(sMsg);
      } finally {
      }

      try {
    	  if (nMilliSecond < 0) {
    		  sMsg = "milli seconds value is invalid, the value is:" + nMilliSecond;
    	  } else {
    		  Thread.sleep(nMilliSecond);
    	  } 	  
      } catch (InterruptedException e) {
          sMsg = e.toString();
          LOGGER.debug(sMsg);
      } finally {
      }
      
      return sMsg;
  }
  
  public void handleIt() throws IOException {
      response.setContentType(MimeTypes.TEXT_PLAIN_UTF_8);    
      final PrintWriter writer = response.getWriter();
      String sMsg = "OK";
      
      String[] types = parameters.get("type");
      if ((null != types) && (null != types[0])) {
    	  String type = types[0];
    	  if ("sleep".equals(type)) {
    	      String[] milliSeconds = parameters.get("milliSeconds");
    		  if (null != milliSeconds) {
    			  sMsg = mySleep(milliSeconds[0]);
    	      }
          } else {
    		  sMsg = "type value is not 'sleep'";
    	  }
      } else {
          sMsg = "type parameter not found or value is empty!";
      }
      
      writer.write(sMsg);
      writer.flush();
  }
}