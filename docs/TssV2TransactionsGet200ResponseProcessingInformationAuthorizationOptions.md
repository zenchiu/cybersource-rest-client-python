# TssV2TransactionsGet200ResponseProcessingInformationAuthorizationOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authorization type.  Possible values:   - **AUTOCAPTURE**: automatic capture.  - **STANDARDCAPTURE**: standard capture.  - **VERBAL**: forced capture. Include it in the payment request for a forced capture. Include it in the capture request for a verbal payment.  **Asia, Middle East, and Africa Gateway; Cielo; Comercio Latino; and CyberSource Latin American Processing**\\ Set this field to _AUTOCAPTURE_ and include it in a bundled request to indicate that you are requesting an automatic capture. If your account is configured to enable automatic captures, set this field to STANDARDCAPTURE and include it in a standard authorization or bundled request to indicate that you are overriding an automatic capture. For more information, see \&quot;Automatic Captures,\&quot; page 33.  **Forced Capture**\\ Set this field to _VERBAL_ and include it in the authorization request to indicate that you are performing a forced capture; therefore, you receive the authorization code outside the CyberSource system. For more information, see \&quot;Forced Captures,\&quot; page 123.  **Verbal Authorization**\\ Set this field to _VERBAL_ and include it in the capture request to indicate that the request is for a verbal authorization. For more information, see \&quot;Verbal Authorizations,\&quot; page 84.  For processor-specific information, see the auth_type field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


